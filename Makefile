.PHONY: demo test

demo:
	python3 projects/01-edge-vibration-monitor/analysis/demo.py

test:
	python3 -m unittest discover -s projects/01-edge-vibration-monitor/tests -v

