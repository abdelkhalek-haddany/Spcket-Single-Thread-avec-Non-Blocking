module com.example.clientmultithreadchat {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.clientmultithreadchat to javafx.fxml;
    exports com.example.clientmultithreadchat;
}