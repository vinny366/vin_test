

var gmailClone=angular.module('example',['ngRoute']);
	
	gmailClone.controller('TestCtrl',function($scope){
		$scope.title="hello";
	})

	gmailClone.config(function ($routeProvider) {
   $routeProvider
      .when('/inbox', {
         templateUrl: 'views/inbox.html',
         controller: 'InboxCtrl',
         controllerAs: 'inbox'
      	})
      .when('/inbox/email/:id', {
         templateUrl: 'views/email.html',
         controller: 'EmailCtrl',
         controllerAs: 'email'
      	})
      .otherwise({
         redirectTo: '/inbox'
     	 });
	});

	
