import radarclient

system_identifier = radarclient.ClientSystemIdentifier('MyApp', '1.0')
radar_client = radarclient.RadarClient(radarclient.AuthenticationStrategySPNego(), system_identifier)