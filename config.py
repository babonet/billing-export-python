"""Configuration file.

Copy to config.py after filling in values.
"""

# runtime configurations
bucket  = billing-166911.appspot.com
default_to_email = oren.maoz@cloudyn.com


# ** OPTIONAL**
#
# Enable dev_appserver.py to use remote GCS bucket
#
# For testing purposes it's can be useful to speak to a remote GCS bucket. If
# this use_remote_gcs_when_local is set to true, additional configurations are
# required when running local dev_servers.
#
use_remote_gcs_when_local = False
#
# To connect to remote GCS rather then remote, create a service account,
#
# similar to abc123abc123@developer.gserviceaccount.com
service_account = '<service-account>'
#
# downloading the private key and changing config.py to reference the private
# key. It's necessary to change .p12 file into a pem file with the command:
#
# > openssl pkcs12 -in abc123abc123-privatekey.p12 -nodes -nocerts | openssl rsa > abc123abc123-privatekey.pem
#
# The password to the key file is "notasecret".
# private key file in local filesystem like 'ABC123-privatekey.pem'
private_key_pem_file =  '<private_key_pem_file>'
