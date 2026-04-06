# Custom Detection Rules — SSH Brute Force & Privilege Escalation

**Date:** 2026-04-06  
**Environment:** Wazuh 4.x single-node, four enrolled agents (citadel, pavilion, annex, inspiron)  
**Objective:** Write, test, and validate custom Wazuh detection rules covering SSH brute force,
Windows failed logon spikes, and unauthorized privilege escalation attempts.

---

## Background

Wazuh ships with hundreds of built-in rules covering common attack patterns. However a core SOC
skill is understanding how to write detection logic tailored to your environment — tuning
thresholds, referencing the correct base rule IDs, and knowing which decoded fields are available
for correlation. This exercise covers that end-to-end: from identifying the correct built-in base
rule IDs to writing correlation rules, validating with wazuh-logtest, and confirming live alerts
in the dashboard.

---

## Rule Architecture — Key Concepts

Before writing rules it is essential to understand how Wazuh chains them.

**`if_sid`** fires your rule when a single event matches the parent rule ID. One event, one alert.
Used for detections where a single occurrence is immediately suspicious — such as an unauthorized
sudo attempt.

**`if_matched_sid`** fires your rule when a parent rule has matched a defined number of times
within a time window. Used for correlation — brute force requires counting repeated failures, not
reacting to a single one.

**`frequency`** and **`timeframe`** are attributes on the rule element itself, not child tags.
A common mistake is placing them as XML child elements — they must be attributes.

**`same_srcip`** groups frequency counts by source IP for Linux events where the decoder
populates the standard `srcip` field.

**`same_field`** groups frequency counts by an arbitrary decoded field. Required for Windows
events where the attacker IP is in `win.eventdata.ipAddress`, not `srcip`. Using `same_srcip`
on Windows correlation rules causes them to never fire — a non-obvious failure mode.

---

## Base Rule Identification

Before writing any correlation rule, identify the actual base rule ID firing for your events.
Never assume a rule ID from documentation — verify it in your environment.

**Method used:** Generated test events (failed SSH logins, failed Windows logons), observed
alerts in Wazuh dashboard → Threat Hunting → Events, noted `rule.id` on each alert.

| Event Type         | Expected Base SID | Actual SID in Lab | Verified                    |
| :----------------- | :---------------- | :---------------- | :-------------------------- |
| SSH invalid user   | 5710              | 5710              | ✅                          |
| SSH auth failure   | 5716              | 5760              | ✅ (5760 fires in this env) |
| Linux sudo failure | 5401              | 5405              | ✅ (5405 fires in this env) |
| Windows 4625       | 60122             | 60122             | ✅                          |

**Key lesson:** The exact base SID that fires depends on your Wazuh version and agent OS.
Rule 5716 was expected for SSH auth failures but 5760 fired instead. Rule 5401 was expected
for sudo but 5405 fired. Always verify before writing correlation rules.

---

## The Rules

All rules live in `/var/ossec/etc/rules/local_rules.xml` on the Wazuh manager.

```xml
<group name="custom,local,">

  <!-- RULE 100001 — SSH Brute Force (invalid user)
       Fires when rule 5710 matches 5 times from the same source IP within 120 seconds.
       Targets attempts against non-existent usernames — common in automated scanning. -->
  <rule id="100001" level="10" frequency="5" timeframe="120">
    <if_matched_sid>5710</if_matched_sid>
    <same_srcip />
    <description>Custom: SSH brute force detected — $(frequency) failed attempts from $(srcip) in $(timeframe)s</description>
    <mitre>
      <id>T1110</id>
    </mitre>
    <group>authentication_failures,ssh_brute_force,</group>
  </rule>

  <!-- RULE 100002 — SSH Auth Failure Spike
       Fires when rule 5760 matches 8 times from the same source IP within 60 seconds.
       Targets rapid auth failures against existing accounts — password spray pattern.
       Higher severity and lower timeframe than 100001 indicates a more aggressive attack. -->
  <rule id="100002" level="12" frequency="8" timeframe="60">
    <if_matched_sid>5760</if_matched_sid>
    <same_srcip />
    <description>Custom: Aggressive SSH auth failures — $(frequency) failures from $(srcip) in $(timeframe)s — possible active brute force</description>
    <mitre>
      <id>T1110</id>
    </mitre>
    <group>authentication_failures,ssh_brute_force,</group>
  </rule>

  <!-- RULE 100003 — Linux Unauthorized Sudo Attempt
       Fires on a single event from rule 5405 — no frequency needed.
       A regular user does not accidentally attempt sudo on commands they lack access to.
       Single-event detection is appropriate — one attempt warrants investigation. -->
  <rule id="100003" level="12">
    <if_sid>5405</if_sid>
    <description>Custom: Unauthorized sudo attempt — user $(dstuser) is not in sudoers on $(hostname)</description>
    <mitre>
      <id>T1548.003</id>
    </mitre>
    <group>privilege_escalation,sudo_attempt,</group>
  </rule>

  <!-- RULE 100004 — Windows Failed Logon Spike
       Fires when rule 60122 (Event ID 4625) matches 5 times from the same source
       IP within 120 seconds.

       IMPORTANT: same_srcip does NOT work for Windows events. The Windows Event Log
       decoder stores the attacker IP in win.eventdata.ipAddress — a dynamic field.
       The standard srcip field is empty for Windows events. same_field must reference
       the correct decoded field directly. Using same_srcip causes this rule to never
       fire — confirmed during testing. -->
  <rule id="100004" level="10" frequency="5" timeframe="120">
    <if_matched_sid>60122</if_matched_sid>
    <same_field>win.eventdata.ipAddress</same_field>
    <description>Custom: Windows failed logon spike — $(frequency) failures from $(win.eventdata.ipAddress) within $(timeframe)s on $(hostname)</description>
    <mitre>
      <id>T1110</id>
    </mitre>
    <group>authentication_failures,windows_brute_force,</group>
  </rule>

</group>
```

---

## Testing Methodology

### Validation Before Deployment

`wazuh-logtest` was used to validate rule syntax and matching logic before restarting the
manager. Sample SSH failure logs were pasted interactively — firedtimes counter was observed
incrementing with each paste, confirming the base rule matched. On the fifth paste, the
correlation rule fired.

Note: `wazuh-logtest -t` is not a valid flag in this Wazuh version. Syntax validation is done
by restarting the manager and checking `systemctl status wazuh-manager` for parse errors.

### Attack Simulation

**Rules 100001 and 100002 — SSH:**

Failed SSH logins were generated from citadel targeting pavilion:

```powershell
for ($i=1; $i -le 6; $i++) { ssh fakeuser@192.168.20.XX 2>$null; Start-Sleep -Milliseconds 500 }
```

For rule 100002 a test user (`testuser`) was created on the target Linux host with a known
password, then rapid SSH failures were generated against it to trigger the existing-user
auth failure path (rule 5760).

**Rule 100003 — Sudo:**

A non-privileged test user was created on the Linux agent. Logged in as that user and
attempted `sudo cat /etc/shadow`. The PAM subsystem logged the unauthorized attempt which
Wazuh decoded via rule 5405 and custom rule 100003 fired.

**Rule 100004 — Windows:**

`net use` was used to generate network logon failures against a remote share, which reliably
populates `win.eventdata.ipAddress` in the Event ID 4625 log — the field required for
`same_field` correlation:

```powershell
for ($i=1; $i -le 6; $i++) {
    net use \\192.168.20.XX\ipc$ /user:fakeuser wrongpassword 2>$null
    Start-Sleep -Milliseconds 500
}
```

Using `Start-Process` or GUI-based credential prompts was found to be unreliable for
populating `win.eventdata.ipAddress` — `net use` is the most consistent method.

---

## Results

| Rule ID | Description                    | Status   | Alert Level | Dashboard Confirmed |
| :------ | :----------------------------- | :------- | :---------- | :------------------ |
| 100001  | SSH brute force — invalid user | ✅ Fired | 10          | ✅                  |
| 100002  | SSH auth failure spike         | ✅ Fired | 12          | ✅                  |
| 100003  | Linux unauthorized sudo        | ✅ Fired | 12          | ✅                  |
| 100004  | Windows failed logon spike     | ✅ Fired | 10          | ✅                  |

---

## Key Lessons Learned

**1. Always verify base rule IDs in your environment.**  
Documentation suggests rule IDs but the actual firing rule depends on your Wazuh version
and agent OS. 5760 fired instead of 5716 for SSH auth failures. 5405 fired instead of 5401
for sudo. Assuming rule IDs without verification leads to correlation rules that silently
never fire.

**2. `same_srcip` does not work for Windows events.**  
This is the most non-obvious failure mode encountered. Windows Event Log events store source
IP in `win.eventdata.ipAddress` — a dynamic decoded field. The standard `srcip` field is
empty. A correlation rule using `same_srcip` will never group Windows events by source IP
and will therefore never reach the frequency threshold. Use `same_field` with the correct
field name instead.

**3. `frequency` and `timeframe` are rule attributes, not child elements.**  
A common XML mistake. These must appear in the opening `<rule>` tag as attributes, not as
separate child tags within the rule body.

**4. Single-event rules don't need frequency or timeframe.**  
Rule 100003 fires on one event because an unauthorized sudo attempt is immediately
suspicious. Over-engineering detection with frequency thresholds where they are not needed
reduces responsiveness and adds complexity.

**5. Test user setup matters for SSH testing.**  
Testing against non-existent users (rule 5710 path) behaves differently from testing
against existing users with wrong passwords (rule 5760 path). Both paths need to be
tested separately if both correlation rules are in scope.
