# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

# limitations under the License.
"""Creates an autoscaled managed instance group."""
# This consists of multiple resources:
# - Instance Template to define the properties for each VM
#      The image and machine size are hardcoded. They could be parameterized
# - Instance Group Manager
# - Autoscaler to grow and shrink the size of the the Instance Group
# - Load Balancer to distribute traffice to the VMs.


URL_BASE = 'https://www.googleapis.com/compute/v1/projects/'

# Every Python Template needs to have the GenerateConfig() or generate_config()
# method
# This method is called by DM in expansion and must return either:
#    - the yaml format required by DM
#    - a python dictionary representing the yaml (this is more efficient)


def GenerateConfig(context):
  """Generates the configuration."""

  deployment = context.env['deployment']
  instance_template = deployment + '-it'
  mgmt = deployment + '-mgmt'
  zone = context.properties['zone']
  port = context.properties['port']

  # Create a dictionary which represents the resources
  # (Intstance Template, IGM, etc.)
  resources = [
      {
          # Create the Instance
          'name': mgmt,
          'type': 'compute.v1.instance',
          'properties': {
              'zone': zone,
              'machineType': ''.join([URL_BASE,
                                  context.env['project'], '/zones/',
                                  context.properties['zone'],
                                  '/machineTypes/n1-standard-4']),
              'tags':{
                  'items': ['http-server']  
              },
              'networkInterfaces': [{
                  'network':
                      URL_BASE + context.env['project'] +
                      '/global/networks/default',
                  'accessConfigs': [{
                      'name': 'External NAT',
                      'type': 'ONE_TO_ONE_NAT'
                      }]
               }],
              'disks': [{
                  'deviceName': 'boot',
                  'type': 'PERSISTENT',
                  'boot': True,
                  'autoDelete': True,
                  'initializeParams': {
                      'diskName': 'disk-' + context.env['deployment'],
                      'sourceImage': URL_BASE + context.properties['image']
                  }
              }]
          }
      }
  ]
  return {'resources': resources}
