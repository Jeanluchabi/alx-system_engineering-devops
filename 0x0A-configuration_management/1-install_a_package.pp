#!/bin/bash/pup

# The Puppet Manifest to install Flask version 2.1.0
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

