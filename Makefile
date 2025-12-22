install:
	uv sync

<<<<<<< HEAD
VD-games:
	uv run vd-games
=======
brain-games:
	uv run VD-games
>>>>>>> dd74827 (Add brain-calc game)

build:
	uv build

package-install:
<<<<<<< HEAD
	uv tool install dist/*.whl

publish-local: build package-install

clean:
	rm -rf dist build *.egg-info
=======
	uv pip install dist/*.whl

link:
	uv run ruff check VD_games

>>>>>>> dd74827 (Add brain-calc game)
