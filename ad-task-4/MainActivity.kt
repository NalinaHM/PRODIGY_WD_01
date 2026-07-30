package com.prodigy.tictactoe

import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.prodigy.tictactoe.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private var isPlayerX = true
    private val board = Array(3) { IntArray(3) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setupGrid()
    }

    private fun setupGrid() {
        val buttons = arrayOf(
            arrayOf(binding.btn00, binding.btn01, binding.btn02),
            arrayOf(binding.btn10, binding.btn11, binding.btn12),
            arrayOf(binding.btn20, binding.btn21, binding.btn22)
        )

        for (r in 0..2) {
            for (c in 0..2) {
                buttons[r][c].setOnClickListener {
                    if (board[r][c] == 0) {
                        board[r][c] = if (isPlayerX) 1 else 2
                        (it as Button).text = if (isPlayerX) "X" else "O"
                        isPlayerX = !isPlayerX
                    }
                }
            }
        }
    }
}
