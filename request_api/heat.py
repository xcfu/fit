# -*- coding: utf-8 -*-

from http_requests import RequestMethod
import json
import settings
from generate_token import keystoneManager
class HeatManager():

    @staticmethod
    def format_url():
        service = settings.protocol + "://" + settings.ip + ":" + settings.heat
        return service


    @classmethod
    def template_versions_list(cls, tenant_id=None):
        url = cls.format_url() + settings.template_versions_list_url.format(tenant_id=tenant_id)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content
	
    @classmethod
    def validate_template(cls, tenant_id=None):
        url = cls.format_url() + settings.template_versions_list_url.format(tenant_id=tenant_id)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def list_stacks(cls, tenant_id=None):
        url = cls.format_url() + settings.list_stacks_url.format(tenant_id=tenant_id)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def show_stacks_details(cls, tenant_id=None, stack_name=None, stack_id=None):
        url = cls.format_url() + settings.show_stack_details_url.format(tenant_id=tenant_id,
                                                                        stack_name = stack_name,
                                                                        stack_id = stack_id)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def suspend_stack(cls, tenant_id=None, stack_name=None, stack_id=None):
        url = cls.format_url() + settings.suspend_stack_url.format(tenant_id=tenant_id,
                                                                   stack_name= stack_name,
                                                                   stack_id = stack_id,

                                                                   )
        response = RequestMethod.post(url = url, data={'suspend':''})
        print "status_code: %s" % response.status_code
        return response.content

class StacksOperation(HeatManager):

    #sequence started with 0
    @classmethod
    def get_stack_id(self,seq):
        tenant_id=keystoneManager.fetch_tenant_id()
        list_stacks = HeatManager.list_stacks(tenant_id=tenant_id)
        list_stacks_len = len(list_stacks['stacks'])

        try:
            if list_stacks_len < seq:
                print "sequence out of range!!"
                return None
            if list_stacks_len>= seq:
                list_stacks_id = list_stacks['stacks'][seq]['id']
                return list_stacks_id
            else:
                print "nothing"
        except Exception,e:
            print Exception, ":", e

    @classmethod
    def get_stack_name(self,seq):
        tenant_id = keystoneManager.fetch_tenant_id()
        list_stacks = HeatManager.list_stacks(tenant_id=tenant_id)
        list_stacks_len = len(list_stacks['stacks'])
        try:
            if list_stacks_len < seq:
                print "sequence out of range!!"
                return None
            if list_stacks_len >= seq:
                return list_stacks['stacks'][seq]['stack_name']
        except Exception, e:
            print Exception, ":", e

