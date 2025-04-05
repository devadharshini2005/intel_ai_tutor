require("dotenv").config();
const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const OpenAI = require("openai");

const app = express();
app.use(express.json());
app.use(cors());

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });

const UserSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  progress: Object,
});

const User = mongoose.model("User", UserSchema);

// User Signup
app.post("/signup", async (req, res) => {
  const { name, email, password } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);
  const user = new User({ name, email, password: hashedPassword, progress: {} });
  await user.save();
  res.json({ message: "User created successfully!" });
});

// User Login
app.post("/login", async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email });
  if (!user || !(await bcrypt.compare(password, user.password))) {
    return res.status(400).json({ error: "Invalid credentials" });
  }
  const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, { expiresIn: "1h" });
  res.json({ token });
});

// AI Tutor Chat
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

app.post("/ask", async (req, res) => {
  const { question } = req.body;
  const response = await openai.chat.completions.create({
    messages: [{ role: "system", content: "You are a personal tutor." }, { role: "user", content: question }],
    model: "gpt-4",
  });
  res.json({ answer: response.choices[0].message.content });
});

app.listen(5000, () => console.log("Backend running on port 5000"));
