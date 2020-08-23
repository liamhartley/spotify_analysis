resource "aws_lambda_function" "spotify_analysis" {
  filename = "../payload.zip"
  function_name = "spotify_analysis"
  handler = "avg_album_length_playlist.lambda_handler"
  role = "${aws_iam_role.lambda_execution_role.arn}"
  runtime = "python3.7"
  timeout = "300"

  environment {
    variables = {
      SPOTIPY_CLIENT_ID = var.TF_VAR_SPOTIPY_CLIENT_ID,
      SPOTIPY_CLIENT_SECRET = var.TF_VAR_SPOTIPY_CLIENT_SECRET
    }
  }
}
