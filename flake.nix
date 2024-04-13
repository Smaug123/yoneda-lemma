{
  description = "Development environment with OpenGL headers";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {
          inherit system;
        };
      in let
        manim-tinytex = pkgs.texliveInfraOnly.withPackages (ps:
          with ps; [
            # tinytex
            amsfonts
            amsmath
            atbegshi
            atveryend
            auxhook
            babel
            bibtex
            bigintcalc
            bitset
            booktabs
            cm
            dehyph
            dvipdfmx
            dvips
            ec
            epstopdf-pkg
            etex
            etexcmds
            etoolbox
            euenc
            everyshi
            fancyvrb
            filehook
            firstaid
            float
            fontspec
            framed
            geometry
            gettitlestring
            glyphlist
            graphics
            graphics-cfg
            graphics-def
            grffile
            helvetic
            hycolor
            hyperref
            hyph-utf8
            iftex
            inconsolata
            infwarerr
            intcalc
            knuth-lib
            kvdefinekeys
            kvoptions
            kvsetkeys
            l3backend
            l3kernel
            l3packages
            latex
            latex-amsmath-dev
            latex-bin
            latex-fonts
            latex-tools-dev
            latexconfig
            latexmk
            letltxmacro
            lm
            lm-math
            ltxcmds
            lua-alt-getopt
            luahbtex
            lualatex-math
            lualibs
            luaotfload
            luatex
            mdwtools
            metafont
            mfware
            natbib
            pdfescape
            pdftex
            pdftexcmds
            plain
            psnfss
            refcount
            rerunfilecheck
            stringenc
            tex
            tex-ini-files
            times
            tipa
            tools
            unicode-data
            unicode-math
            uniquecounter
            url
            xcolor
            xetex
            xetexconfig
            xkeyval
            xunicode
            zapfding

            # manim-latex
            standalone
            everysel
            preview
            doublestroke
            ms
            setspace
            rsfs
            relsize
            ragged2e
            fundus-calligra
            microtype
            wasysym
            physics
            dvisvgm
            jknapltx
            wasy
            cm-super
            babel-english
            gnu-freefont
            mathastext
            cbfonts-fd
          ]);
      in let
        pythonEnv = pkgs.python3.withPackages (ps: [
          ps.numpy
          ps.pycairo
          ps.pip
          ps.mapbox-earcut
          ps.scipy
          ps.srt
          ps.pygments
          ps.requests
        ]);
      in {
        devShell = pkgs.mkShell {
          buildInputs =
            (
              if pkgs.stdenv.isDarwin
              then [
                pkgs.darwin.apple_sdk.frameworks.OpenGL
                pkgs.darwin.apple_sdk.frameworks.ApplicationServices
                pkgs.darwin.apple_sdk.frameworks.Carbon
              ]
              else []
            )
            ++ [
              pythonEnv
              pkgs.cairo
              pkgs.pango
              pkgs.pkg-config
              pkgs.glib
              pkgs.ffmpeg
              pkgs.nodePackages.markdown-link-check
              pkgs.alejandra
              manim-tinytex
              pkgs.pyright
            ];
        };
      }
    );
}
