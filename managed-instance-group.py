"""Creates a managed instance group."""


# This will be used to build the Web and App Tiers

def GenerateConfig(context):
  """Generates the configuration."""

# Create a dictionary which represents the resources

  resources = [
      {
          'name': context.env['name'],
          'type': 'compute.v1.regionInstanceGroupManager',
          'properties': {
              'region': context.properties[‘region’],
              'baseInstanceName': context.env['name'],
              'instanceTemplate': 
                  context.properties['instanceTemplate'],
              'targetSize': 1,
              'autoHealingPolicies': [{
                  'initialDelaySec': 60
              }]
          }
      }
  ]
return {'resources': resources}
