#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: vcenter_vm_hardware_adapter_scsi
short_description: Adds a virtual SCSI adapter to the virtual machine.
description: Adds a virtual SCSI adapter to the virtual machine.
options:
    adapter:
        description:
        - Virtual SCSI adapter identifier.
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi).
            Required with I(state=['absent', 'present'])
        type: str
    bus:
        description:
        - SCSI bus number.
        - If unset, the server will choose an available bus number; if none is available,
            the request will fail.
        type: int
        default: 0
    label:
        description:
        - The name of the item
        type: str
    pci_slot_number:
        description:
        - Address of the SCSI adapter on the PCI bus. If the PCI address is invalid,
            the server will change it when the VM is started or as the device is hot
            added.
        - If unset, the server will choose an available address when the virtual machine
            is powered on.
        type: int
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    sharing:
        choices:
        - NONE
        - PHYSICAL
        - VIRTUAL
        description:
        - The I(sharing) enumerated type defines the valid bus sharing modes for a
            virtual SCSI adapter.
        type: str
    state:
        choices:
        - absent
        - present
        default: present
        description: []
        type: str
    type:
        choices:
        - BUSLOGIC
        - LSILOGIC
        - LSILOGICSAS
        - PVSCSI
        description:
        - The I(type) enumerated type defines the valid emulation types for a virtual
            SCSI adapter.
        type: str
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that run the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
    vm:
        description:
        - Virtual machine identifier.
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.vcenter_vm_info).
            This parameter is mandatory.
        required: true
        type: str
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 0.1.0
requirements:
- vSphere 7.0.3 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.3
"""

EXAMPLES = r"""
- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info

- name: Create a SCSI adapter at PCI slot 35
  vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 35
  register: _scsi_adapter_result_1

- name: Drop the SCSI controller
  vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 35
    state: absent
  register: _result
"""
RETURN = r"""
# content generated by the update_return_section callback# task: Create a SCSI adapter at PCI slot 35
id:
  description: moid of the resource
  returned: On success
  sample: '1000'
  type: str
value:
  description: Create a SCSI adapter at PCI slot 35
  returned: On success
  sample:
    label: SCSI controller 0
    pci_slot_number: 35
    scsi:
      bus: 0
      unit: 7
    sharing: NONE
    type: PVSCSI
  type: dict
"""


# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "delete": {"query": {}, "body": {}, "path": {"adapter": "adapter", "vm": "vm"}},
    "update": {
        "query": {},
        "body": {"sharing": "sharing"},
        "path": {"adapter": "adapter", "vm": "vm"},
    },
    "create": {
        "query": {},
        "body": {
            "bus": "bus",
            "pci_slot_number": "pci_slot_number",
            "sharing": "sharing",
            "type": "type",
        },
        "path": {"vm": "vm"},
    },
}  # pylint: disable=line-too-long

from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    open_session,
    prepare_payload,
    session_timeout,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["adapter"] = {"type": "str"}
    argument_spec["bus"] = {"type": "int", "default": 0}
    argument_spec["label"] = {"type": "str"}
    argument_spec["pci_slot_number"] = {"type": "int"}
    argument_spec["sharing"] = {
        "type": "str",
        "choices": ["NONE", "PHYSICAL", "VIRTUAL"],
    }
    argument_spec["state"] = {
        "type": "str",
        "choices": ["absent", "present"],
        "default": "present",
    }
    argument_spec["type"] = {
        "type": "str",
        "choices": ["BUSLOGIC", "LSILOGIC", "LSILOGICSAS", "PVSCSI"],
    }
    argument_spec["vm"] = {"required": True, "type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return (
        "https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/adapter/scsi"
    ).format(**params)


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _create(params, session):

    lookup_url = per_id_url = build_url(params)
    uniquity_keys = ["adapter"]
    comp_func = None

    async def lookup_with_filters(params, session, url):
        search_filter = ""

        if "name" not in params:
            return
        async with session.get(f"{url}?names={params['name']}{search_filter}") as resp:
            _json = await resp.json()
            if isinstance(_json, list) and len(_json) == 1:
                return await get_device_info(session, url, _json[0]["adapter"])

    _json = None

    if params["adapter"]:
        _json = await get_device_info(session, build_url(params), params["adapter"])

    if not _json and (uniquity_keys or comp_func):
        _json = await exists(
            params,
            session,
            url=lookup_url,
            uniquity_keys=uniquity_keys,
            per_id_url=per_id_url,
            comp_func=comp_func,
        )

    if not _json:
        _json = await lookup_with_filters(params, session, build_url(params))

    if _json:
        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}
        if "_update" in globals():
            params["adapter"] = _json["id"]
            return await globals()["_update"](params, session)

        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = (
        "https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/adapter/scsi"
    ).format(**params)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}

        if (resp.status in [200, 201]) and "error" not in _json:
            if isinstance(_json, str):  # 7.0.2 and greater
                _id = _json  # TODO: fetch the object
            elif isinstance(_json, dict) and "value" not in _json:
                _id = list(_json["value"].values())[0]
            elif isinstance(_json, dict) and "value" in _json:
                _id = _json["value"]
            _json_device_info = await get_device_info(session, _url, _id)
            if _json_device_info:
                _json = _json_device_info

        return await update_changed_flag(_json, resp.status, "create")


async def _delete(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["delete"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["delete"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        "/api/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.delete(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


async def _update(params, session):
    payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = (
        "https://{vcenter_hostname}"
        "/api/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}"
    ).format(**params)
    async with session.get(_url, **session_timeout(params)) as resp:
        _json = await resp.json()
        if "value" in _json:
            value = _json["value"]
        else:  # 7.0.2 and greater
            value = _json
        for k, v in value.items():
            if k in payload:
                if isinstance(payload[k], dict) and isinstance(v, dict):
                    to_delete = True
                    for _k in list(payload[k].keys()):
                        if payload[k][_k] != v.get(_k):
                            to_delete = False
                    if to_delete:
                        del payload[k]
                elif payload[k] == v:
                    del payload[k]
                elif payload[k] == {}:
                    del payload[k]

        if payload == {} or payload == {"spec": {}}:
            # Nothing has changed
            if "value" not in _json:  # 7.0.2
                _json = {"value": _json}
            _json["id"] = params.get("adapter")
            return await update_changed_flag(_json, resp.status, "get")
    async with session.patch(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        # e.g: content_configuration
        if not _json and resp.status == 204:
            async with session.get(_url, **session_timeout(params)) as resp_get:
                _json_get = await resp_get.json()
                if _json_get:
                    _json = _json_get

        _json["id"] = params.get("adapter")
        return await update_changed_flag(_json, resp.status, "update")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(current_loop)
        current_loop.run_until_complete(main())
    finally:
        current_loop.close()
