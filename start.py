import subprocess

# FastAPI Server Configuration
FASTAPI_HOST = "0.0.0.0"  # Bind to all network interfaces
FASTAPI_PORT = "8000"

# Cloudflare Tunnel Configuration
CLOUDFLARE_TUNNEL_NAME = "farmsync-tunnel"

if __name__ == "__main__":
    try:
        # Start FastAPI
        fastapi_process = subprocess.Popen(
            ["uvicorn", "app.main:app", "--host", FASTAPI_HOST, "--port", FASTAPI_PORT, "--reload"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # Start Cloudflare Tunnel
        cloudflare_process = subprocess.Popen(
            ["cloudflared", "tunnel", "run", CLOUDFLARE_TUNNEL_NAME],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # Print real-time output from both processes
        while True:
            fastapi_output = fastapi_process.stdout.readline()
            cloudflare_output = cloudflare_process.stdout.readline()
            
            if fastapi_output:
                print(fastapi_output, end="")
            if cloudflare_output:
                print(cloudflare_output, end="")

            if fastapi_process.poll() is not None and cloudflare_process.poll() is not None:
                break
    except KeyboardInterrupt:
        print("\n🛑 Stopping services...")
        fastapi_process.terminate()
        cloudflare_process.terminate()
        print("✅ Services stopped successfully!")