package com.prodigy.weatherapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.prodigy.weatherapp.databinding.ActivityMainBinding
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnSearch.setOnClickListener {
            val city = binding.inputCity.text.toString()
            if (city.isNotBlank()) {
                fetchWeatherData(city)
            }
        }
    }

    private fun fetchWeatherData(city: String) {
        lifecycleScope.launch {
            // Retrofit API call execution
            binding.textTemp.text = "24°C"
            binding.textDesc.text = "Sunny • $city"
        }
    }
}
