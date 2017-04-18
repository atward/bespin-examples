from bespin.actions import an_action
from bespin.operations.deployer import Deployer
from bespin.operations.builder import Builder

import logging

log = logging.getLogger("vibrato.custom")

@an_action(needs_credentials=True)
def deploy_all(collector, **kwargs):
    stacks = collector.configuration["stacks"]
    made = []
    checked = []
    deployer = Deployer()

    # XXX: does this need more order logic other than layers?
    for index, layer in enumerate(Builder().layered(stacks)):
        for _, stack in layer:
            deployer.deploy_stack(stack, stacks, made=made, checked=checked)


def __bespin__(bespin, task_maker):
    task_maker("deploy_all", "deploy all stacks in layered order")
