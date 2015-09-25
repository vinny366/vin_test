
  angular.module('example')
  .controller('InboxCtrl',
    function InboxCtrl ( $scope, InboxFactory ) {
      'use strict';
      $scope.meta = {
        title: "My Inbox"
      };
    });