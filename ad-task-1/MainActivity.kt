package com.prodigy.unitconverter

import android.os.Bundle
import android.widget.ArrayAdapter
import androidx.appcompat.app.AppCompatActivity
import androidx.core.widget.addTextChangedListener
import com.prodigy.unitconverter.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    private val lengthUnits = arrayOf("Meters", "Feet", "Kilometers", "Miles", "Inches")
    private val lengthRates = mapOf(
        "Meters" to 1.0,
        "Feet" to 3.28084,
        "Kilometers" to 0.001,
        "Miles" to 0.000621371,
        "Inches" to 39.3701
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, lengthUnits)
        binding.spinnerFrom.adapter = adapter
        binding.spinnerTo.adapter = adapter

        binding.inputVal.addTextChangedListener { doConversion() }
    }

    private fun doConversion() {
        val input = binding.inputVal.text.toString().toDoubleOrNull() ?: 0.0
        val from = binding.spinnerFrom.selectedItem.toString()
        val to = binding.spinnerTo.selectedItem.toString()

        val base = input / (lengthRates[from] ?: 1.0)
        val result = base * (lengthRates[to] ?: 1.0)

        binding.resultText.text = String.format("%.2f %s", result, to)
    }
}
