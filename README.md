\# SOC-Style Security Log Analysis Toolkit



\## Overview

This project demonstrates a Security Operations Center (SOC) style approach

to analyzing authentication logs and detecting suspicious login behavior

using rule-based anomaly detection.



The focus is on analyst thinking, log interpretation, and clear reporting

rather than tool-heavy automation.



---



\## Problem Statement

Organizations generate large volumes of authentication logs daily.

Manually identifying malicious login activity such as brute-force attacks

is inefficient and error-prone. Automated log analysis is essential for

early threat detection.



---



\## Detection Approach

The project implements the following detection techniques:



\- Analysis of failed vs successful login attempts

\- Time-window based correlation of authentication failures

\- IP and username relationship analysis

\- Severity classification based on frequency of failures

\- Identification of potential brute-force behavior



---



\## Data Source

Synthetic authentication logs modeled after real-world Windows/Linux

login events. The dataset includes realistic timestamps, usernames,

IP addresses, and authentication outcomes.



---



\## Tools \& Technologies

\- Python

\- Pandas

\- Matplotlib

\- Jupyter Notebook

\- Git \& GitHub



---



\## Project Structure



