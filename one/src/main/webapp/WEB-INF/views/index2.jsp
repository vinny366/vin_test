<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>

<html>
<body>
<h2>Hello World!</h2>

I am feeling: ${ mood.feeling }.

<a href="one/${ mood.feeling }"> get reasons </a>
</body>
</html>