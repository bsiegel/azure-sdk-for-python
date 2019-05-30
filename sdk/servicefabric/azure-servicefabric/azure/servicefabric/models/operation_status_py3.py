# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OperationStatus(Model):
    """Contains the OperationId, OperationState, and OperationType for
    user-induced operations.

    :param operation_id: A GUID that identifies a call to this API.  This is
     also passed into the corresponding GetProgress API.
    :type operation_id: str
    :param state: The state of the operation. Possible values include:
     'Invalid', 'Running', 'RollingBack', 'Completed', 'Faulted', 'Cancelled',
     'ForceCancelled'
    :type state: str or ~azure.servicefabric.models.OperationState
    :param type: The type of the operation. Possible values include:
     'Invalid', 'PartitionDataLoss', 'PartitionQuorumLoss', 'PartitionRestart',
     'NodeTransition'
    :type type: str or ~azure.servicefabric.models.OperationType
    """

    _attribute_map = {
        'operation_id': {'key': 'OperationId', 'type': 'str'},
        'state': {'key': 'State', 'type': 'str'},
        'type': {'key': 'Type', 'type': 'str'},
    }

    def __init__(self, *, operation_id: str=None, state=None, type=None, **kwargs) -> None:
        super(OperationStatus, self).__init__(**kwargs)
        self.operation_id = operation_id
        self.state = state
        self.type = type