## Debug no browser

Caso deseje fazer debug da aplicação no próprio navegador ao invés da IDE, antes de construir a imagem no docker, vá pra o aplicativo `app.py` e troque a linha:

```
app.run(debug=False, host="0.0.0.0")
```
por
```
app.run(debug=True, host="127.0.0.1")
```

## Links

Hospedado atualmente nos seguintes domínios:
  * Render (master): https://tributary-tunic-yin-dzvp.onrender.com/
  * Render (Google-sheets): https://dash-la-google-sheets.onrender.com
## Referências

### Dash AG Grid
 
[https://dash.plotly.com/dash-ag-grid](https://dash.plotly.com/dash-ag-grid) 

[https://www.ag-grid.com/](https://www.ag-grid.com/)

 ### Dash Mantine docs

 [https://www.dash-mantine-components.com/](https://www.dash-mantine-components.com/)
