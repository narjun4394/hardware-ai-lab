# Exact Bill of Materials

Selected on June 6, 2026 for a guarded, low-voltage desk prototype. Prices are
planning estimates before tax and shipping; verify them when ordering.

## Required Parts

| Qty | Exact part | Planning cost | Selection rationale |
| ---: | --- | ---: | --- |
| 1 | [Espressif ESP32-S3-DevKitC-1-N8R8](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-DEVKITC-1-N8R8/15295894) | USD 15 | The official board provides an ESP32-S3, 8 MB flash, 8 MB octal PSRAM, exposed GPIO, and separate USB-to-UART and native USB ports. It leaves room for data capture and later edge inference. |
| 1 | [SparkFun Triple Axis Accelerometer Breakout - ADXL345, SEN-09836](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-adxl345.html) | USD 25 | The documented breakout supports SPI, selectable ranges through +/-16 g, and output data rates up to 3,200 Hz. Buying the named board avoids the quality uncertainty of very cheap ADXL345 clones. |
| 1 | [Noctua NF-A8 5V PWM](https://noctua.at/en/nf-a8-5v-pwm) | USD 20 | This enclosed-frame 80 mm fan runs from 5 V, exposes PWM speed control and a tachometer signal, and includes a USB power adaptor cable. The frame gives the sensor and safety guards repeatable mounting points. |
| 1 pack | [Noctua NA-FG1-8 Sx2 fan grills](https://noctua.at/en/na-fg1-8-sx2) | USD 15 | Front and rear steel grills reduce accidental contact with the rotating blades while preserving access to the fan frame. |
| 1 | [Noctua NA-FC1 PWM fan controller](https://www.noctua.at/en/na-fc1/specification) | USD 25 | The controller is documented for Noctua 5 V PWM fans and can sit between the fan's USB adaptor and the fan, providing repeatable speed changes without building a 5 V PWM interface during the first milestone. |
| 1 | USB-C data cable for ESP32-S3 | USD 8 | Powers the development board and carries serial data to the laptop. Use a known data-capable cable. |
| 1 set | Female-to-female 2.54 mm jumper wires | USD 7 | Connects the populated breakout header to the development board during the first prototype. |
| 1 strip | 2.54 mm male breakaway header | USD 2 | Provides pins for the SparkFun breakout if the selected listing arrives without headers installed. |
| 1 roll | Removable double-sided mounting tape | USD 6 | Provides a repeatable starter mounting method without drilling the fan frame. A rigid bracket is the planned upgrade after data collection works. |
| 4 | Identical self-adhesive rubber feet, at least 10 mm tall | USD 5 | Holds the guarded fan above the desk for airflow and creates a repeatable reference mount. Measure and record the delivered foot dimensions. |

**Required-parts planning total: USD 128**

The fan receives power through its included USB adaptor cable and the NA-FC1.
The ESP32-S3 receives power from a separate USB cable connected to the laptop. No
battery or high-voltage supply is required.

A soldering station, solder, safety glasses, multimeter, and hand tools are
assumed available. Add them to the order if they are not already on the bench.

## Procurement Plan

Target order date: **June 8, 2026**. Target date to have the complete rig ready
for assembly: **June 19, 2026**.

| Part group | Preferred source | Delivery planning assumption |
| --- | --- | --- |
| ESP32-S3-DevKitC-1-N8R8 | DigiKey | Order only when shown in stock; allow 3-7 business days |
| SparkFun ADXL345 breakout | SparkFun | Order only when shown in stock; allow 3-7 business days |
| Noctua fan and guards | Authorized US Noctua retailer | Allow 3-7 business days |
| Cable, jumpers, mounting tape, and rubber feet | Local stock or electronics retailer | Allow 1-7 business days |

These are schedule targets, not vendor promises. Record the actual seller,
checkout price, order date, and promised delivery date in this table before
placing an order. Do not substitute an unknown ADXL345 breakout merely to save a
few days.

## Optional Validation and Upgrade Parts

| Qty | Exact part | Planning cost | Why it is optional |
| ---: | --- | ---: | --- |
| 1 | [ST STEVAL-MKI208V1K evaluation kit with IIS3DWB](https://www.st.com/en/evaluation-tools/steval-mki208v1k.html) | USD 40 | The IIS3DWB is designed for vibration monitoring and has a flat frequency response through 6 kHz. Use it later to measure what the lower-bandwidth ADXL345 misses. |
| 1 | USB inline power meter | USD 15 | Useful for recording the prototype's current draw during sampling and inference. |
| 1 | Small solderless breadboard | USD 6 | Useful only if a tachometer pull-up, PWM level circuit, or other interface components are added. |

## Hardware Constraints

- Configure the ADXL345 for SPI and a 3,200 Hz output data rate.
- Use a 1,024-sample window, producing one window every 0.32 seconds.
- The ADXL345 bandwidth at the maximum output data rate is about 1.6 kHz. This is
  suitable for a learning prototype, not a claim of industrial fault coverage.
- Sample all three axes and record the fan tachometer when possible.
- Use the fan at a fixed speed for baseline captures before testing multiple
  speeds.
- Do not power the fan from an ESP32-S3 GPIO pin or the board's 3.3 V rail.
- Verify every delivered part number and connector before wiring. Vendor listings
  and delivery dates can change.

## References

- [ESP32-S3-DevKitC-1 user guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/index.html)
- [ESP32-S3-DevKitC-1-N8R8 ordering page](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-DEVKITC-1-N8R8/15295894)
- [SparkFun ADXL345 product page and documents](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-adxl345.html)
- [Analog Devices ADXL345 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl345.pdf)
- [Noctua NF-A8 5V PWM specifications](https://noctua.at/en/nf-a8-5v-pwm/specification)
- [Noctua NA-FG1-8 Sx2 specifications](https://noctua.at/en/na-fg1-8-sx2/specification)
- [Noctua guidance for using the NA-FC1 with 5 V USB fans](https://faqs.noctua.at/en/support/solutions/articles/101000353337-can-the-na-fc1-be-used-with-5v-usb-12v-and-24v-fans-)
- [ST IIS3DWB product page](https://www.st.com/en/mems-and-sensors/iis3dwb.html)
