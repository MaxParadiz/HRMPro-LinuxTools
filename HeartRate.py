import gatt

manager = gatt.DeviceManager(adapter_name='hci0')

class AnyDevice(gatt.Device):
    def services_resolved(self):
        super().services_resolved()

        HR_service = next(
            s for s in self.services
            if s.uuid == '0000180d-0000-1000-8000-00805f9b34fb')

        HR_characteristic = next(
            c for c in HR_service.characteristics
            if c.uuid == '00002a37-0000-1000-8000-00805f9b34fb')

        HR_characteristic.enable_notifications()

    def characteristic_value_updated(self, characteristic, value):
        print(value[1])


device = AnyDevice(mac_address='AA:BB:CC:DD:EE:FF', manager=manager)
device.connect()

manager.run()
