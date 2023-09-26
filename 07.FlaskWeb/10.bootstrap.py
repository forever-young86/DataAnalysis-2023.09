from flask import Flask, render_template, request
import util.crawl_util as cu
import util.map_util as mu

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>부트스트랩</h1>'

@app.route('/list')
def list():
    return render_template('10.list.html')   

@app.route('/form')
def form():
    return render_template('10.form.html')

@app.route('/modal')
def modal():
    return render_template('10.modal.html')

@app.route('/interpark')
def interpark():
    book_list = cu.get_bestseller()
    return render_template('10.interpark.html', book_list=book_list)

@app.route('/cctv_pop', methods=['GET','POST'])
def cctv_pop():
    if request.method == 'GET':
        columns = ['CCTV댓수','최근증가율','인구수','내국인','외국인','고령자','외국인 비율','고령자 비율']
        colormaps = ['RdPu', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
        return render_template('10.cctv_pop_form.html', columns=columns, colormaps=colormaps)
    else:
        column = request.form['column']
        colormap = request.form['colormap']
        mu.get_cctv_pop(app.static_folder, column, colormap)
        return render_template('10.cctv_pop_res.html', column=column, colormap=colormap)


if __name__ == '__main__':
    app.run(debug=True) 