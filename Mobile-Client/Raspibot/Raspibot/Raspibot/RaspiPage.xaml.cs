using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Raspibot
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class RaspiPage
	{
		public RaspiPage ()
		{
			InitializeComponent ();
            PiView.Source = new HtmlWebViewSource
            {
                Html = "<html>\n\n<head>\n  <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\" integrity=\"sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO\" crossorigin=\"anonymous\">\n  <style>\n    body{\n      max-width: 720px;\n      max-height: 480px;\n    }\n  </style>\n</head>\n\n<body>\n  <div class=\"container\">\n    <img src=\"http://192.168.0.105:8081/\" />\n  </div>\n</body>\n</html>\n"
            };
		}
	}
}