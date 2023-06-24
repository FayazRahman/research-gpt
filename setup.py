from setuptools import setup, find_packages

package_name = "researchgpt"

install_requires = ["loopgpt"]
extras_require = {}

if __name__ == "__main__":
    setup(
        install_requires=install_requires,
        extras_require=extras_require,
        packages=find_packages(),
        name=package_name,
        version="0.0.1",
        description="Modular Auto-GPT Framework",
        entry_points={"console_scripts": ["loopgpt = loopgpt.loops.cli:main"]},
    )
