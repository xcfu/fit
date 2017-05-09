# -*- coding: utf-8 -*-

from request_api.heat import HeatManager,StacksOperation
from generate_token import keystoneManager



number = input("please input the sequence of stack:")

stack = StacksOperation
stack_id = stack.get_stack_id(seq=number)
stack_name = stack.get_stack_name(seq=number)

print "the No.%s stack's name is %s and it's stack id is %s" % (number,stack_name,stack_id)


#get stacks list include id,name
tenant_id = keystoneManager.fetch_tenant_id()
list_stacks = HeatManager.list_stacks(tenant_id=tenant_id)
list_stacks_len = len(list_stacks['stacks'])

stack_id = ['']*list_stacks_len
stack_name = ['']*list_stacks_len
if list_stacks_len == 0:
    print "No stack!!"
elif list_stacks_len != 0:
    for i in range(list_stacks_len):
        stack_id[i] = list_stacks['stacks'][i]['id']
        stack_name[i] = list_stacks['stacks'][i]['stack_name']
        print "the No.%s stack id is %s" % (i,stack_id[i])

#get detail of all stacks
for i in range(list_stacks_len):

    stack_details = HeatManager.show_stacks_details(tenant_id=tenant_id,
                                                    stack_name=stack_name[i],
                                                    stack_id=stack_id[i])
    print stack_details

# suspend_stack = HeatManager.suspend_stack(tenant_id=tenant_id,
#                                          stack_name=u'auto-test',
#                                          stack_id=u'13a44031-fa64-4d4a-bb37-a4736ca9f132',
#                                          )
# print suspend_stack
