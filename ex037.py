{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ex037.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMGPIatTMjXXbc7OlBmrjPv",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/joaomarcosrs/PythonExercicios/blob/master/ex037.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KUCEO6I5N5vv",
        "outputId": "aa88a506-b44d-4026-9e0d-624617372944"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um núemro: 10\n",
            "Digite o número da opção que você deseja\n",
            "\n",
            "[ 1 ] converter para Binário\n",
            "[ 2 ] converter para Octal\n",
            "[ 3 ] converter para Hexadecimal\n",
            "\n",
            "Digite a opção de conversão: 2\n",
            "\n",
            "\n",
            "O número convertido para Octal é: 12\n"
          ]
        }
      ],
      "source": [
        "numero = int(input('Digite um núemro: '))\n",
        "print('''Digite o número da opção que você deseja\n",
        "\n",
        "[ 1 ] converter para Binário\n",
        "[ 2 ] converter para Octal\n",
        "[ 3 ] converter para Hexadecimal\n",
        "''')\n",
        "op = int(input('Digite a opção de conversão: '))\n",
        "print('\\n')\n",
        "\n",
        "if op == 1:\n",
        "  print('O número convertido para Binário é: {}'.format(format(numero, 'b')))\n",
        "elif op == 2:\n",
        "  print('O número convertido para Octal é: {}'.format(format(numero, 'o')))\n",
        "else:\n",
        "  numero = format(numero, 'x')\n",
        "  numero = str(numero)\n",
        "  print('O número convertido para Hexadecimal é: {}'.format(numero.upper()))\n"
      ]
    }
  ]
}