# Instance Template to define the properties for each VM
# The image and machine size are hardcoded. They could be parameterized

# Every Python Template needs to have the GenerateConfig() or generate_config()
# method
# This method is called by DM in expansion and must return either:
#    - the yaml format required by DM
#    - a python dictionary representing the yaml (this is more efficient)

def GenerateConfig(context):
  """Generates the configuration."""
  
  URL_SUBNETS = 'https://www.googleapis.com/compute/v1/projects/' + context.env['project'] + '/regions/' + context.properties['region'] + '/subnetworks/'
  URL_IMAGES = 'https://www.googleapis.com/compute/v1/projects/' + context.env['project'] + '/global/images/'

  # Create a dictionary which represents the resources
  # (Intstance Template, IGM, etc.)
  resources = [
      {
          'name': context.env['name'] + '-template',
          'type': 'instance-template.py',
            'properties': {
              'region': context.properties['region'],
              'machineType': context.properties['machineType'],
              'tags': context.properties['tags'],
              'subnetwork': URL_SUBNETS + context.properties['subnetwork'],
              'sourceImage': URL_IMAGES + context.properties['sourceImage'],
              'diskSize': context.properties['diskSize']
            }
      },
     {
          'name': context.env['name'] + '-ig',
          'type': 'managed-instance-group.py',
            'properties': {
              'region': context.properties['region'],
              'instanceTemplate': ''.join(['$(ref.',context.env['name'],'-template.selfLink)'])
            }
     }
  ]
  return {'resources': resources}
