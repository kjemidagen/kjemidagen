//using Kjemidagen.Models;
//using Kjemidagen.Helpers;
//using Microsoft.AspNetCore.Mvc;

//namespace Kjemidagen.Controllers
//{
//    [ApiController]
//    [Route("Company")]
//    public class CompanyController : ControllerBase
//    {
//        private static readonly string[] Names = new[]
//        {
//            "Borregaard", "Ventura", "Accenture", "NTNU", "Sintef", "SpeletOmSognOgFjordane"
//        };

//        private readonly ILogger<CompanyController> _logger;

//        public CompanyController(ILogger<CompanyController> logger)
//        {
//            _logger = logger;
//        }

//        [HttpGet()]
//        public IEnumerable<Company> Get()
//        {
//            return Enumerable.Range(1, 5).Select(index => new Company
//            {
//                ID = index,
//                Name = Names[Random.Shared.Next(Names.Length)],
//                HashedPassword = Hamlet.GeneratePassword(15)+Random.Shared.Next(100),
//                EmailAddress = Hamlet.GeneratePassword(1) + "@" + Hamlet.GeneratePassword(1) + ".com",
//                NumberOfCompanyRepresentatives = Random.Shared.Next(1, 10),
//                Information = "No information"
//            })
//            .ToArray();
//        }
//    }
//}