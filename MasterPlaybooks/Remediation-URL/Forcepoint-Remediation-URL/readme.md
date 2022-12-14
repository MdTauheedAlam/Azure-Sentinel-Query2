# Forcepoint NGFW Block URL Nested Remediation Playbook

## Summary
 When  this playbook is triggered and it performs the below actions:
 1. Gets list of potentially malicious URLs.
 2. For each URL in the list, checks if the URL is already present in URL List Name or not.
 3. List of all URLs not present in URL List Name is blocked in the firewall by the playbook.

 ## Pre-requisites for deployment
 1. Deploy the Forcepoint SMC Custom Connector before the deployment of this playbook under the same subscription and same resource group as will be used for this playbook. Capture the name of the connector during deployment.
 2. Forcepoint SMC API Key should be known to establish a connection with Forcepoint SMC. For API Key [Refer here](http://www.websense.com/content/support/library/ngfw/v610/rfrnce/ngfw_6100_ug_smc-api_a_en-us.pdf )
 3. Forcepoint SMC Version number should be known. [Refer here](https://help.stonesoft.com/onlinehelp/StoneGate/SMC/) to download and install Forcepoint SMC and capture the version number for the same.
 4. URLs list name for blocking URL present in SMC should be known.

 ### Deploy Custom Connector

To deploy ForcepointNGFW Custom connector click on the below button.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FPlaybooks%2FForcepointNGFW%2FForcepointSMCApiConnector%2Fazuredeploy.json)  [![Deploy to Azure Gov](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FPlaybooks%2FForcepointNGFW%2FForcepointSMCApiConnector%2Fazuredeploy.json) 


 ## Deployment Instructions
 1. Deploy the playbook by clicking on the "Deploy to Azure" button. This will take you to deploy an ARM Template wizard.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Ftree%2Fmaster%2FMasterPlaybooks%2FRemediation-URL%2FForcepoint-Remediation-URL%2Fazuredeploy.json) [![Deploy to Azure](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Ftree%2Fmaster%2FMasterPlaybooks%2FRemediation-URL%2FForcepoint-Remediation-URL%2Fazuredeploy.json)

 2. Fill in the required parameters for deploying the playbook.

 | Parameter  | Description |
| ------------- | ------------- |
| **Playbook Name** | Enter the Playbook Name here without spaces. (e.g. BlockIP-Forcepoint ) |
| **Forcepoint SMC Connector name**|Enter the name of your Forcepoint SMC Connector without spaces.|
| **Forcepoint SMC API Key**  | Enter the SMC API Key. | 
| **Forcepoint SMC Version Number** | Enter the version number of SMC. (e.g. 6.9) |
| **URL List Name**|Enter URLs list name.|




# Playbook steps explained
## When this playbook is triggered
  Captures potentially malicious or malware IP addresses incident information.

## Compose image to add in the incident
This action will compose the Forcepoint image to add to the incident comments.

## For each malicious URL received from the incident

### Check if URL is present in URL List Name
* If URL is present in URL List Name then check if URL List is part of security policy rule.
* If URL is not present in URL List Name then add the URL to URL List Name. Incident comment created with URL blocked by Playbook.

### Check if URL List is part of security policy in SMC
*  If a security policy exists in the SMC firewall for URL List Name then URL is already blocked. Incident comment created with URL already blocked.
*  If the security policy does not exist for URL List name then security policy is created for URL List Name.

## Response from playbook is sent to master playbook to generate incident comments.



