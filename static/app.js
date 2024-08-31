var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $http) {
    $scope.formData   = {};
    $scope.custFname  = ""; // Holds the response text from Flask
    $scope.customerID = "";
    $scope.custLname  = "";
    $scope.birthdate  = "";
    $scope.gender     = "";

    $scope.submitForm = function() {
        $http.post('/submit', $scope.formData)
        .then(function(response) {
            // Update responseText with the server's response
            $scope.customerID = response.data.CustID || "No response message";
            $scope.custFname  = response.data.FirstName || "No response message";
            $scope.custLname  = response.data.LastName || "No response message";
            $scope.birthdate  = response.data.BirthDate || "No response message";
            $scope.gender     = response.data.Gender || "No response message";
        
            console.log("Server Response:", response.data);
        }, function(error) {
            // Handle error response
            $scope.responseText = "Error submitting form!";
            console.error("Submission Error:", error);
        });
    };
});
