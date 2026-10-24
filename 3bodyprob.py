import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------- RESOLUTION ----------
print("Choose resolution:")
print("1: HD (1800x1000)")
print("2: 4K (3840x2160)")
print("3: 8K (7680x4320)")
res = input("Enter choice (1-3): ")

if res == "1":
    WIDTH, HEIGHT = 1800, 1000
elif res == "2":
    WIDTH, HEIGHT = 3840, 2160
elif res == "3":
    WIDTH, HEIGHT = 7680, 4320
else:
    WIDTH, HEIGHT = 1800, 1000

# ---------- MODE ----------
print("\nChoose 3-body system:")
print("1: Random")
print("2: Lagrange")
print("3: Figure-eight")
print("4: Binary + satellite")
print("5: Cinematic collision")
print("6: Predefined binary")
print("7: User-defined")
choice = input("Enter choice (1-7): ")

# ---------- INITIAL CONDITIONS ----------
if choice == "1":
    pos = np.random.uniform(-5, 5, (3, 2))
    vel = np.random.uniform(-0.4, 0.4, (3, 2))
    G = 1.0

elif choice == "2":
    pos = np.array([[0,2], [-1.732,-1], [1.732,-1]])
    vel = np.array([[0.5,0], [-0.25,0.43], [-0.25,-0.43]])
    G = 1.0

elif choice == "3":
    pos = np.array([[1,0], [-1,0], [0,0]])
    vel = np.array([[0.25,0.25], [0.25,0.25], [-0.5,-0.5]])
    G = 1.0

elif choice == "4":
    pos = np.array([[-2,0], [2,0], [0,1]])
    vel = np.array([[0,0.35], [0,-0.35], [-0.25,0]])
    G = 1.0

elif choice == "5":  # Cinematic collision
    pos = np.array([[-3.0,  0.0],
                    [ 3.0,  0.0],
                    [ 0.0,  2.2]])
    vel = np.array([[ 0.18,  0.22],
                    [-0.18, -0.22],
                    [ 0.00, -0.12]])
    G = 0.55

elif choice == "6":
    pos = np.array([[-3,0], [3,0], [0,0.6]])
    vel = np.array([[0,0.3], [0,-0.3], [0.15,0]])
    G = 1.0

elif choice == "7":
    pos = np.zeros((3,2))
    vel = np.zeros((3,2))
    for i in range(3):
        pos[i] = list(map(float, input(f"Enter x y for body {i+1}: ").split()))
        vel[i] = list(map(float, input(f"Enter vx vy for body {i+1}: ").split()))
    G = 1.0

else:
    exit()

pos = pos.astype(float)
vel = vel.astype(float)

# ---------- PHYSICS ----------
dt_normal = 0.008
dt_slow = 0.002
dt = dt_normal
steps = 3500

def acceleration(p):
    a = np.zeros_like(p)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = p[j] - p[i]
                d = np.linalg.norm(r) + 1e-4
                a[i] += G * r / d**3
    return a

# ---------- TRAILS ----------
trail_len = 180 if choice == "5" else 90
history = [[] for _ in range(3)]
debris = []
collision_triggered = False

# ---------- PLOT ----------
fig, ax = plt.subplots(figsize=(WIDTH/100, HEIGHT/100))
ax.set_facecolor("black")
ax.set_xlim(-8,8)
ax.set_ylim(-8,8)
ax.set_xticks([])
ax.set_yticks([])

stars = [ax.plot([], [], 'o', markersize=8)[0] for _ in range(3)]
trails = [ax.plot([], [], lw=1, alpha=0.6)[0] for _ in range(3)]

colors = ["gold", "cyan", "magenta"]
for i in range(3):
    stars[i].set_color(colors[i])
    trails[i].set_color(colors[i])

# ---------- UPDATE ----------
def update(frame):
    global pos, vel, debris, dt, collision_triggered

    vel += acceleration(pos) * dt
    pos += vel * dt

    for i in range(3):
        history[i].append(pos[i].copy())
        if len(history[i]) > trail_len:
            history[i].pop(0)
        h = np.array(history[i])
        stars[i].set_data([pos[i,0]], [pos[i,1]])
        trails[i].set_data(h[:,0], h[:,1])

    return stars + trails

# ---------- RUN ----------
ani = FuncAnimation(fig, update, frames=steps, interval=20, blit=False)
plt.show()
