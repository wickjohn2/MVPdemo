#Build Application Tier from Components

def GenerateConfig(context):
  # Generates the configuration."""

  # Create a dictionary which represents the resources

  resources = [
      {
          'name': context.env['name'],
          'type': 'compute.v1.regionAutoscaler',
          'properties': {
              'target': context.properties['managedInstanceGroup'],
              'region': context.properties['region'],
              'autoscalingPolicy': {
                  'minNumReplicas': context.properties['minSize'],
                  'maxNumReplicas': context.properties['maxSize'],
                  'cpuUtilization': {
                      'utilizationTarget': 
                          context.properties['cpuUtil']
                  },
                  'coolDownPeriodSec': 90
              }
          }
      }
  ]
return {'resources': resources}
