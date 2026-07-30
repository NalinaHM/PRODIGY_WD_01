package com.prodigy.taskmanager

import android.os.Bundle
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import com.prodigy.taskmanager.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private val viewModel: TaskViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val adapter = TaskAdapter { task -> viewModel.toggleTask(task) }
        binding.recyclerView.adapter = adapter

        binding.btnAdd.setOnClickListener {
            val text = binding.inputTask.text.toString()
            if (text.isNotBlank()) {
                viewModel.addTask(TaskEntity(title = text))
                binding.inputTask.text?.clear()
            }
        }

        viewModel.allTasks.observe(this) { tasks ->
            adapter.submitList(tasks)
        }
    }
}
