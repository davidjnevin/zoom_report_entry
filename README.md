# Zoom report entry generator

On occassion I need to generate a time range for a zoom meeting for testing.
This script, given a start time and date, and duration generates a zoom report entry in the format below. 

|email|jointime|leavetime|duration|
|:----------|:----------|:----------|----------:|
| xxxxx@gmail.com	| 02/25/2025 03:31:54 PM | 02/25/2025 05:02:05 PM	| 91 |
| |	02/25/2025 03:36:55 PM | 02/25/2025 03:37:12 PM |	1 |
| |	02/25/2025 03:37:13 PM | 02/25/2025 04:55:28 PM |	79 |

There is an element of randomness introduced to reflect realistic join times and leavetimes. 

This version generates for one guest.
