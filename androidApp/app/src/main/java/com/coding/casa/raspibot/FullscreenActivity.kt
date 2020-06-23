package com.coding.casa.raspibot

import android.annotation.SuppressLint
import android.os.Bundle
import android.os.Handler
import androidx.appcompat.app.AppCompatActivity
import com.longdo.mjpegviewer.MjpegView
import io.github.controlwear.virtual.joystick.android.JoystickView
import kotlinx.android.synthetic.main.activity_fullscreen.*
import java.io.DataInputStream
import java.io.DataOutputStream
import java.lang.Exception
import java.net.InetSocketAddress
import java.net.Socket


/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 */
class FullscreenActivity : AppCompatActivity(), JoystickView.OnMoveListener {
    private var botSocket: Socket? = null
    private var outputStreamWriter: DataOutputStream? = null
    private val hideHandler = Handler()

    private var isFullscreen: Boolean = false

    private val hideRunnable = Runnable { hide() }

    @SuppressLint("ClickableViewAccessibility")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_fullscreen)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        isFullscreen = true
        val runnable = Runnable {
            botSocket = Socket()
            connect()
        }
        Thread(runnable).start()
        piBotView.mode = MjpegView.MODE_FIT_WIDTH
        piBotView.isAdjustHeight = true
        piBotView.setUrl("http://192.168.86.169:8000/stream.mjpg")
        piBotView.startStream()
        joystick.setOnMoveListener(this)
    }

    private fun connect() {
        do {
            try {
                botSocket!!.connect(InetSocketAddress("192.168.86.169", 9000), 60)
                outputStreamWriter = DataOutputStream(botSocket!!.getOutputStream())
            }catch (e: Exception){
                print(e.message)
            }
        }while (!botSocket!!.isConnected || outputStreamWriter == null)
    }
    private fun sendMessage(message: String) {
        Thread {
            if(!botSocket!!.isConnected || outputStreamWriter == null){
                connect()
            }
            outputStreamWriter!!.writeBytes("$message\n")
            outputStreamWriter!!.flush()
        }.start()
    }

    override fun onPostCreate(savedInstanceState: Bundle?) {
        super.onPostCreate(savedInstanceState)
        delayedHide(1)
    }

    private fun hide() {
        // Hide UI first
        supportActionBar?.hide()
        isFullscreen = false

    }

    private fun delayedHide(delayMillis: Int) {
        hideHandler.removeCallbacks(hideRunnable)
        hideHandler.postDelayed(hideRunnable, delayMillis.toLong())
    }

    override fun onResume() {
        super.onResume()
        if(botSocket == null) {
            Thread{
                botSocket = Socket()
                connect()
            }.start()
        }
        piBotView.mode = MjpegView.MODE_FIT_WIDTH
        piBotView.isAdjustHeight = true
        piBotView.setUrl("http://192.168.86.169:8000/stream.mjpg")
        piBotView.startStream()
    }
    override fun onDestroy() {
        sendMessage("disconnect")
        outputStreamWriter?.close()
        botSocket?.close()
        botSocket = null
        super.onDestroy()
    }

    override fun onPause() {
        sendMessage("disconnect")
        outputStreamWriter?.close()
        botSocket?.close()
        botSocket = null
        super.onPause()
    }

    companion object {
        /**
         * Whether or not the system UI should be auto-hidden after
         * [AUTO_HIDE_DELAY_MILLIS] milliseconds.
         */
        private const val AUTO_HIDE = true

        /**
         * If [AUTO_HIDE] is set, the number of milliseconds to wait after
         * user interaction before hiding the system UI.
         */
        private const val AUTO_HIDE_DELAY_MILLIS = 3000

        /**
         * Some older devices needs a small delay between UI widget updates
         * and a change of the status and navigation bar.
         */
        private const val UI_ANIMATION_DELAY = 300
    }

    override fun onMove(angle: Int, strength: Int) {
        if(strength <= 20){
            sendMessage("stop")
        }
        if(angle in 0..180){
            if(angle in 1..89) {
                sendMessage("forward")
                sendMessage("right")
            }
            if(angle in 91..179) {
                sendMessage("forward")
                sendMessage("left")
            }
            if(angle == 90) {
                sendMessage("forward")
            }
            if(angle == 180) {
                sendMessage("left")
            }
            if(angle == 0) {
                sendMessage("right")
            }
        }
        if(angle in 180..360){
            if(angle in 181..269) {
                sendMessage("backward")
                sendMessage("left")
            }
            if(angle in 271..359) {
                sendMessage("backward")
                sendMessage("right")
            }
            if(angle == 270) {
                sendMessage("backward")
            }
            if(angle == 180) {
                sendMessage("left")
            }
            if(angle == 0) {
                sendMessage("right")
            }
        }
    }
}