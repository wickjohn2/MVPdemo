# Instance Template to define the properties for each VM
# The image and machine size are hardcoded. They could be parameterized

# Every Python Template needs to have the GenerateConfig() or generate_config()
# method
# This method is called by DM in expansion and must return either:
#    - the yaml format required by DM
#    - a python dictionary representing the yaml (this is more efficient)

def GenerateConfig(context):
  """Generates the configuration."""

  # Create a dictionary which represents the resources
  # (Intstance Template, IGM, etc.)
  resources = [
      {
          'name': context.env['name'],
          'type': 'instance-template.py',
            'properties': {
              'region': context.properties['region'],
              'machineType': context.properties['machineType'],
              'tags': context.properties['tags'],
              'subnetwork': context.properties['subnetwork'],
              'sourceImage': context.properties['sourceImage'],
              'diskSize': context.properties['diskSize']
            }
      }
  ]
  return {'resources': resources}
