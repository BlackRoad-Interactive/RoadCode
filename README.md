# BlackRoad-Interactive — RoadCode

> Games, Metaverse & 3D division of [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc)

Game engine, physics simulation, 3D rendering, and metaverse worlds. Built for real-time interactive experiences that run on your device, your data, your agents.

## Products

| Product | What It Does |
|---------|-------------|
| **Genesis Road** | Game engine — entity-component system, scene graph, asset pipeline |
| **RoadWorld** | Metaverse platform — isometric pixel worlds, multiplayer, NPC agents |
| **Physics Engine** | Rigid body dynamics, collision detection, spatial partitioning |
| **3D Renderer** | WebGL/WebGPU renderer with shader library |

## Org Hierarchy

```
BlackRoad-OS-Inc (Parent — 254 repos, 67 agents, 7 nodes)
  └── BlackRoad-Interactive (Games & 3D)
      ├── RoadCode          ← this repo (workspace + automation)
      ├── game-engine        ← Genesis Road core
      ├── interactive-core   ← shared runtime + ECS
      ├── physics-engine     ← collision + dynamics
      ├── 3d-renderer        ← WebGL/WebGPU pipeline
      ├── operator           ← CLI tools + build scripts
      └── source             ← canonical source tree
```

## Repos in This Org

- [`RoadCode`](https://github.com/BlackRoad-Interactive/RoadCode) — Workspace hub (this repo)
- [`game-engine`](https://github.com/BlackRoad-Interactive/game-engine) — Genesis Road game engine
- [`interactive-core`](https://github.com/BlackRoad-Interactive/interactive-core) — Shared ECS runtime
- [`physics-engine`](https://github.com/BlackRoad-Interactive/physics-engine) — Physics simulation
- [`3d-renderer`](https://github.com/BlackRoad-Interactive/3d-renderer) — Rendering pipeline
- [`operator`](https://github.com/BlackRoad-Interactive/operator) — CLI + deployment
- [`source`](https://github.com/BlackRoad-Interactive/source) — Source tree

## How It Connects

- **Parent**: [BlackRoad-OS-Inc](https://github.com/BlackRoad-OS-Inc) — central coordination
- **AI**: [BlackRoad-AI](https://github.com/BlackRoad-AI) — NPC behavior powered by local Ollama models
- **Hardware**: [BlackRoad-Hardware](https://github.com/BlackRoad-Hardware) — Hailo-8 for real-time inference in gameplay
- **Studio**: [BlackRoad-Studio](https://github.com/BlackRoad-Studio) — Asset creation pipeline feeds into game worlds
- **Pixel HQ**: 14-floor metaverse HQ with 50 pixel art assets on R2

## License

Proprietary — BlackRoad OS, Inc. See [LICENSE](./LICENSE).

---

*Remember the Road. Pave Tomorrow.*
