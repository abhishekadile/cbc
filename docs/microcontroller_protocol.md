# Microcontroller Protocol

Serial 115200 baud, 8N1.

**Commands**
- `HOME`: Homes XYZ
- `MOVE X=<um> Y=<um>`: Moves stage
- `FOCUS Z=<um>`: Moves focus
- `LED CH=<channel>`: Sets LED channel
- `TRIGGER ID=<capture_id>`: Triggers capture
- `STATUS`: Gets status
- `ESTOP`: Emergency stop

**Responses**
- `OK`
- `DONE ID=<capture_id>`
- `ERR <message>`
