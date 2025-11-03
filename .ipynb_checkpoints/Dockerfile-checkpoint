# Step 1: Start from an official Python base image.
# We use "slim" because it's a smaller, more production-ready image
# than the full Python image, which saves space.
FROM python:3.9-slim

# Step 2: Set a working directory inside the container.
# This is where our app's code will live. All future commands
# like `COPY` and `RUN` will happen relative to this `/app` directory.
WORKDIR /app

# Step 3: Copy the requirements file first, by itself.
# This is a key Docker optimization. Docker builds in "layers".
# By copying only this file, Docker will only re-run the
# slow 'pip install' step IF this file changes. If you only
# change 'api.py', the build will use a cache for this layer,
# making it much faster.
COPY requirements.txt .

# Step 4: Install all the Python dependencies.
# We use --no-cache-dir to make the final image smaller
# by not storing the pip download cache.
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the api.py file into current directory
COPY api.py .

# Step 6: Expose the port the API will run on.
# This tells Docker that the container will listen on port 8080.
EXPOSE 8080

# Step 7: Define the command to run when the container starts.
# This is the "main" command for the container. It runs your
# FastAPI app using the uvicorn server..
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]