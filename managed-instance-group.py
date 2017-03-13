"""Creates a managed instance group."""

# Create Instance Group Manager

URL_BASE = 'https://www.googleapis.com/compute/v1/projects/'

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
          'type': 'compute.v1.regionInstanceGroupManager',
          'properties': {
              'region': context.properties['region'],
              'baseInstanceName': context.env['name'],
              'instanceTemplate': context.properties['instanceTemplate'],
              'targetSize': 1,
              'autoHealingPolicies': [{
                  'initialDelaySec': 60
              }]
          }
      }
  ]
  return: {'resources': resources}
