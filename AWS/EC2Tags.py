from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.cloudformation.checks.resource.base_resource_check import BaseResourceCheck


class EC2Tags(BaseResourceCheck):
    def __init__(self):
        name = "Ensure EC2 Instance configured with tags"
        id = "CKV2_AWS_1001"
        supported_resources = ['AWS::EC2::Instance']
        # CheckCategories are defined in models/enums.py
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'Properties' in conf.keys():
            if 'Tags' not in conf['Properties'].keys():
                return CheckResult.FAILED
        return CheckResult.PASSED


scanner = EC2Tags()
