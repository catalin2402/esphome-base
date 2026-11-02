# ESPHome Base

ESPHome configuration packages for ESP32, ESP8266, BK72xx and RP2 devices.

Required substitutions use `REPLACEME`. Optional overrides show their default values.

## Base configurations

| Package | Description | Required substitutions | Optional overrides (defaults) |
| --- | --- | --- | --- |
| `base.yaml` | Wi-Fi, API, OTA, logging, web server, restart buttons, IP address and uptime text. | `name`<br>`friendly_name`<br>`area`<br>`wifi_password`<br>`wifi_ssid` | `logger_baud_rate: 0` |
| `base-static.yaml` | Wi-Fi base with a static IP address. | `name`<br>`friendly_name`<br>`area`<br>`wifi_password`<br>`wifi_ssid`<br>`wifi_gateway`<br>`wifi_ip`<br>`wifi_subnet` | `logger_baud_rate: 0` |
| `base-no-wifi.yaml` | Base services without Wi-Fi configuration. | `name`<br>`friendly_name`<br>`area` | `logger_baud_rate: 0` |
| `base-ap-only.yaml` | Access-point mode with a captive portal. | `name`<br>`friendly_name`<br>`area`<br>`wifi_password` | `logger_baud_rate: 0` |

## Core and networking

| Package | Description | Required substitutions | Optional overrides (defaults) |
| --- | --- | --- | --- |
| `core/device.yaml` | Device name, friendly name and area. | `name`<br>`friendly_name`<br>`area` | — |
| `core/services.yaml` | API, OTA, safe mode, logging and restart buttons. | — | `logger_baud_rate: 0` |
| `core/web-server.yaml` | Local web interface. | — | — |
| `network/wifi.yaml` | Wi-Fi connection. | `wifi_password`<br>`wifi_ssid` | — |
| `network/wifi-static.yaml` | Static IP settings. | `wifi_gateway`<br>`wifi_ip`<br>`wifi_subnet` | — |
| `network/wifi-recovery.yaml` | Fallback access point and captive portal. | `wifi_password`<br>`name` | — |
| `network/ap-only.yaml` | Access-point-only configuration. | `wifi_password`<br>`name` | — |
| `network/w5500.yaml` | W5500 Ethernet using dedicated SPI pins. | `pin_eth_clk`<br>`pin_eth_cs`<br>`pin_eth_interrupt`<br>`pin_eth_miso`<br>`pin_eth_mosi`<br>`pin_eth_reset` | `ethernet_clock_speed: 8MHz`<br>`ethernet_cs_ignore_strapping_warning: false`<br>`ethernet_interrupt_ignore_strapping_warning: false` |
| `network/w5500-shared-spi.yaml` | W5500 Ethernet using an existing SPI bus. | `pin_eth_cs`<br>`pin_eth_interrupt`<br>`pin_eth_reset` | `ethernet_clock_speed: 8MHz`<br>`ethernet_cs_ignore_strapping_warning: false`<br>`ethernet_interrupt_ignore_strapping_warning: false` |

## Diagnostics and status

| Package | Description | Required substitutions | Optional overrides (defaults) |
| --- | --- | --- | --- |
| `diagnostics/wifi.yaml` | Wi-Fi IP address. | — | — |
| `diagnostics/ethernet.yaml` | Ethernet IP address. | — | — |
| `diagnostics/wifi-signal.yaml` | Wi-Fi signal strength. | — | `wifi_signal_update_interval: 60s` |
| `diagnostics/status.yaml` | Connection status. | — | — |
| `diagnostics/uptime-text.yaml` | Uptime as formatted text. | — | — |
| `diagnostics/uptime.yaml` | Uptime as a numeric value. | — | — |
| `status/led.yaml` | Status LED. | `pin_status_led` | `status_led_inverted: true`<br>`status_led_allow_other_uses: false` |
| `status/light.yaml` | Status LED with light controls. | `pin_status_led` | `status_led_inverted: true`<br>`status_led_allow_other_uses: false` |
| `debug/debug-esp32.yaml` | ESP32 device and memory diagnostics. | — | `debug_update_interval: 5s` |
| `debug/debug-esp8266.yaml` | ESP8266 device and memory diagnostics. | — | `debug_update_interval: 5s` |
| `debug/debug-bk72xx.yaml` | BK72xx device and memory diagnostics. | — | `debug_update_interval: 5s` |
| `debug/debug-rp2.yaml` | RP2 device diagnostics. | — | `debug_update_interval: 5s` |
| `debug/common.yaml` | Basic device, memory and performance diagnostics. | — | `debug_update_interval: 5s` |
| `debug/psram-esp32.yaml` | ESP32 PSRAM diagnostics. | — | — |

## Sensors

| Package | Description | Required substitutions | Optional overrides (defaults) |
| --- | --- | --- | --- |
| `sensors/bme280.yaml` | Temperature, humidity and pressure. | `bme280_address` | — |
| `sensors/bmp280.yaml` | Temperature and pressure. | `bmp280_address` | — |
| `sensors/dht.yaml` | DHT temperature and humidity. | `pin_dht` | — |
| `sensors/dallas.yaml` | Dallas 1-Wire temperature sensor. | `dallas_address`<br>`pin_dallas` | — |
| `sensors/htu21d.yaml` | HTU21D temperature and humidity. | — | — |
| `sensors/hlw8012.yaml` | Power, voltage, current and daily energy. | `hlw8012_current_resistor`<br>`hlw8012_voltage_divider`<br>`pin_hlw8012_cf`<br>`pin_hlw8012_cf1`<br>`pin_hlw8012_sel` | `hlw8012_update_interval: 30s`<br>`hlw8012_current_min_voltage: 1.0` |

## Lighting, fans and helpers

| Package | Description | Required substitutions | Optional overrides (defaults) |
| --- | --- | --- | --- |
| `hardware/sm2135-rgbww.yaml` | SM2135 RGB and white-channel lighting. | `pin_sm2135_clk`<br>`pin_sm2135_data` | `sm2135_cw_current: 15mA`<br>`sm2135_rgb_current: 20mA`<br>`sm2135_cold_white_temperature: 6536 K`<br>`sm2135_warm_white_temperature: 2000 K` |
| `fan/three-speed-relay.yaml` | Three-speed fan controlled by interlocked relays. | `pin_button_high`<br>`pin_button_low`<br>`pin_button_medium`<br>`pin_relay_high`<br>`pin_relay_low`<br>`pin_relay_medium` | `fan_relay_inverted: false`<br>`fan_interlock_wait_time: 500ms`<br>`fan_switching_delay: 100ms` |
| `light-effects/light.yaml` | Lighting effects. | — | — |
| `light-effects/fade-3.yaml`, `fade-7.yaml` | Three- and seven-color fade effects. | `id` (include variable) | — |
| `light-effects/jump-3.yaml`, `jump-7.yaml` | Three- and seven-color jump effects. | `id` (include variable) | — |
| `helpers/motion_light.yaml` | Motion-controlled lighting with dimming and shutoff. | `motion_light_id`<br>`pin_motion` | `motion_light_on_brightness: 0.98`<br>`motion_first_delay: 5s`<br>`motion_intermediate_brightness: 0.48`<br>`motion_second_delay: 3s` |
| `helpers/binary_motion_light.yaml` | Motion-controlled lighting with selectable shutoff delays. | `motion_delay_sensor_id`<br>`motion_light_id`<br>`pin_motion` | `motion_first_delay: 30s`<br>`motion_second_delay: 5min` |
| `helpers/on_boot_switch.yaml` | Sets the indicator to match a switch at startup. | `pin_status_led`<br>`on_boot_switch_id` | `status_led_inverted: true`<br>`status_led_allow_other_uses: false` |

## Cameras, displays and time

| Package | Description | Required substitutions | Optional overrides (defaults) |
| --- | --- | --- | --- |
| `camera/camera.yaml` | ESP32 camera and flash light. | `pin_camera_data_1`<br>`pin_camera_data_2`<br>`pin_camera_data_3`<br>`pin_camera_data_4`<br>`pin_camera_data_5`<br>`pin_camera_data_6`<br>`pin_camera_data_7`<br>`pin_camera_data_8`<br>`pin_camera_ext_clock`<br>`pin_camera_href`<br>`pin_camera_i2c_scl`<br>`pin_camera_i2c_sda`<br>`pin_camera_pixel_clock`<br>`pin_camera_power_down`<br>`pin_camera_vsync`<br>`pin_flash` | `camera_max_framerate: 10 fps`<br>`camera_resolution: 800x600`<br>`camera_ext_clock: 20MHz` |
| `camera/camera-servos.yaml` | Camera pan and tilt controls. | `pin_servo_1`<br>`pin_servo_2` | `default_servo_pan: 0`<br>`default_servo_tilt: 0` |
| `display/pcf8574_font.yaml` | Large clock characters for a PCF8574 LCD. | — | — |
| `time/ha.yaml` | Time from Home Assistant. | — | — |
| `time/sntp.yaml` | Time from an SNTP server. | — | — |

## IR remotes

| Package | Description | Required substitutions | Optional overrides (defaults) |
| --- | --- | --- | --- |
| `remote/generic-24-key-ct.yaml` | Generic 24-key lighting remote with color-temperature controls. | — | — |
| `remote/generic-44-key.yaml` | Generic 44-key lighting remote. | — | — |
| `remote/hoff-24-key.yaml` | Hoff 24-key lighting remote. | — | — |
| `remote/kaufland-24-key.yaml` | Kaufland 24-key lighting remote. | — | — |
| `remote/magic-lighting-24-key.yaml` | Magic Lighting 24-key remote. | — | — |
