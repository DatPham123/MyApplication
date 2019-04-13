package edu.uco.dpham9.myapplication;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;
import android.widget.MediaController;
import android.widget.Toast;
import android.widget.VideoView;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class MainActivity extends AppCompatActivity {

    Button playBtn;
    Button stopBtn;
    Button upBtn;
    Button downBtn;
    Button feedBtn;
    EditText textIP;
    private WebView webView;
    public static String wifiModuleIp ="";
    public static int wifiModulePort = 0;
    public static String CMD = "0";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        playBtn = (Button) findViewById(R.id.id_play);
        stopBtn = (Button) findViewById(R.id.id_stop);
        feedBtn = (Button) findViewById(R.id.id_btn_feed);
        textIP = (EditText) findViewById(R.id.id_ip);
        final MediaController mediacontroller = new MediaController(this);
        webView = (WebView) findViewById(R.id.id_web_view);
        webView.setWebViewClient(new WebViewClient());

        playBtn.setEnabled(true);
        stopBtn.setEnabled(false);
        webView.setVisibility(View.GONE);

        feedBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                getIPandPort();
                CMD="F";
                Socket_Async cmd_feed_servo = new Socket_Async();
                cmd_feed_servo.execute();
            }
        });

        playBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                webView.loadUrl("Replace_IP_HERE:8000/stream.mp4");
                webView.setVisibility(View.VISIBLE);
                playBtn.setEnabled(false);
                stopBtn.setEnabled(true);
            }
        });

        stopBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                webView.stopLoading();
                webView.setVisibility(View.GONE);
                playBtn.setEnabled(true);
                stopBtn.setEnabled(false);
            }
        });

    }

    public void getIPandPort(){
        String iPandPort = textIP.getText().toString();
        Log.d("TEST", "IP string: " + iPandPort);
        String temp[] = iPandPort.split(":");
        wifiModuleIp = temp[0];
        wifiModulePort = Integer.valueOf(temp[1]);
        Log.d("TEST", "IP: " + wifiModuleIp);
        Log.d("TEST", "PORT: " + wifiModulePort);

    }

    public class Socket_Async extends AsyncTask<Void, Void, Void>{

        Socket socket;

        @Override
        protected Void doInBackground(Void... params) {
            try{
                InetAddress inetAddress = InetAddress.getByName(MainActivity.wifiModuleIp);
                socket = new java.net.Socket(inetAddress,MainActivity.wifiModulePort);
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
                dataOutputStream.writeBytes(CMD);
                dataOutputStream.close();
                //socket.close();
            }catch (UnknownHostException e){
                e.printStackTrace();
            }catch (IOException e){
                e.printStackTrace();
            }

            return null;
        }
    }
































}
