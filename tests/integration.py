# -*- coding: utf-8 -*-

import pytest

from guardrail.core import exceptions


class PermissionManagerMixin(object):

    def test_crud(self):

        manager, agent, target = self.manager, self.agent, self.target

        assert not manager.has_permission(agent, target, 'read')
        assert not manager.has_permission(agent, target, 'write')
        assert not manager.get_permissions(agent, target)

        manager.add_permission(agent, target, 'read')
        manager.add_permission(agent, target, 'write')

        assert manager.has_permission(agent, target, 'read')
        assert manager.has_permission(agent, target, 'write')
        assert manager.get_permissions(agent, target) == {'read', 'write'}

        manager.remove_permission(agent, target, 'write')

        assert manager.has_permission(agent, target, 'read')
        assert not manager.has_permission(agent, target, 'write')
        assert manager.get_permissions(agent, target) == {'read'}

        with pytest.raises(exceptions.PermissionNotFound):
            manager.remove_permission(agent, target, 'write')

        with pytest.raises(exceptions.PermissionExists):
            manager.add_permission(agent, target, 'read')
