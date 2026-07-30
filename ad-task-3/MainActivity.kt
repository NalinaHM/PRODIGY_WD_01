package com.prodigy.quizapp

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.prodigy.quizapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private var currentScore = 0
    private var currentQuestionIndex = 0

    private val questions = listOf(
        QuizQuestion(1, "Official language for Android?", listOf("Java", "Kotlin", "C++", "Python"), 1),
        QuizQuestion(2, "Component handling UI layout rendering?", listOf("BroadcastReceiver", "Activity", "Service", "ContentProvider"), 1),
        QuizQuestion(3, "SQLite database management library?", listOf("Room DB", "Retrofit", "Glide", "WorkManager"), 0)
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        displayQuestion()
    }

    private fun displayQuestion() {
        val q = questions[currentQuestionIndex]
        binding.questionText.text = q.questionText
        binding.btnOption1.text = q.options[0]
        binding.btnOption2.text = q.options[1]
        binding.btnOption3.text = q.options[2]
        binding.btnOption4.text = q.options[3]
    }

    fun onOptionSelected(selectedIndex: Int) {
        val q = questions[currentQuestionIndex]
        if (selectedIndex == q.correctAnswerIndex) {
            currentScore += 10
            Toast.makeText(this, "Correct! +10", Toast.LENGTH_SHORT).show()
        }
        currentQuestionIndex = (currentQuestionIndex + 1) % questions.size
        displayQuestion()
    }
}
